import torch

from AgentPPO import AgentPPO
from Config import Config
from run import train_agent

MODELS = {"ppo": AgentPPO}
OFF_POLICY_MODELS = ["ddpg", "td3", "sac"]
ON_POLICY_MODELS = ["ppo"]

class DRLAgent:
    """Implementations of DRL algorithms
    Attributes
    ----------
        env: gym environment class
            user-defined class
    Methods
    -------
        get_model()
            setup DRL algorithms
        train_model()
            train DRL algorithms in a train dataset
            and output the trained model
        DRL_prediction()
            make a prediction in a test dataset and get results
    """

    def __init__(self, env, price_array, tech_array, turbulence_array, date_array):
            self.env = env
            self.price_array = price_array
            self.tech_array = tech_array
            self.turbulence_array = turbulence_array
            self.date_array = date_array

    def get_model(self, model_name, model_kwargs):
        env_config = {
            "price_array": self.price_array,
            "tech_array": self.tech_array,
            "turbulence_array": self.turbulence_array,
            "date_array": self.date_array,
            "if_train": True,
        }
        environment = self.env(config=env_config)
        env_args = {'config': env_config,
              'env_name': environment.env_name,
              'state_dim': environment.state_dim,
              'action_dim': environment.action_dim,
              'if_discrete': False,
        }
        agent = MODELS[model_name]
        if model_name not in MODELS:
            raise NotImplementedError("NotImplementedError")
        model = Config(agent_class=agent, env_class=self.env, env_args=env_args)
        model.if_off_policy = model_name in OFF_POLICY_MODELS
        if model_kwargs is not None:
            try:
                model.learning_rate = model_kwargs["learning_rate"]
                model.batch_size = model_kwargs["batch_size"]
                model.gamma = model_kwargs["gamma"]
                model.seed = model_kwargs["seed"]
                model.net_dim = model_kwargs["net_dimension"]
                model.target_step = model_kwargs["target_step"]
                model.eval_gap = model_kwargs["eval_gap"]
                model.eval_times = model_kwargs["eval_times"]
                model.weight_decay = model_kwargs["weight_decay"]
                model.lambda_entropy = model_kwargs["lambda_entropy"]
            except BaseException:
                raise ValueError(
                    "Fail to read arguments, please check 'model_kwargs' input."
                )
        return model

    def train_model(self, model, cwd, total_timesteps=5000):
        model.cwd = cwd
        model.break_step = total_timesteps
        train_agent(model)

    @staticmethod
    def DRL_prediction(model_name, cwd, net_dimension, environment):
        if model_name not in MODELS:
            raise NotImplementedError("NotImplementedError")
        agent_class = MODELS[model_name]
        environment.env_num = 1
        agent = agent_class(net_dimension, environment.state_dim, environment.action_dim)
        actor = agent.act
        # load agent
        try:  
            cwd = cwd + '/actor.pth'
            print(f"| load actor from: {cwd}")
            actor.load_state_dict(torch.load(cwd, map_location=lambda storage, loc: storage))
            act = actor
            device = agent.device
        except BaseException:
            raise ValueError("Fail to load agent!")

        # test on the testing env
        _torch = torch
        state, _ = environment.reset()
        episode_returns = []  # the cumulative_return / initial_account
        episode_total_assets = [environment.initial_total_assets]
        episode_dates = []
        with _torch.no_grad():
            for i in range(environment.max_step):
                s_tensor = _torch.as_tensor((state,), device=device)
                a_tensor = act(s_tensor)  # action_tanh = act.forward()
                action = (
                    a_tensor.detach().cpu().numpy()[0]
                )  # not need detach(), because with torch.no_grad() outside
                state, reward, done, _, _ = environment.step(action)
                episode_dates.append(environment.date_ary[environment.current_step])
                total_assets = (
                    environment.cash
                    + (
                        environment.price_ary[environment.current_step] * environment.stocks
                    ).sum()
                )
                episode_total_assets.append(total_assets)
                episode_return = total_assets / environment.initial_total_assets
                episode_returns.append(episode_return)
                if done:
                    break
        num_trades = environment.num_trades
        print("Test Finished!")
        # return episode total_assets on testing data
        print("episode_return", episode_return)
        return episode_dates, episode_total_assets, episode_return, num_trades