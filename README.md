# autopilot-sandbox

autopilot 全链路演练用的沙盒仓库。这里配到"接管到合并"（`.github/autopr/takeover.yml`），由本机编排以机器人 `haigeerlab-autopilot[bot]` 的身份跑审查、检查、写证据、合并；撤回、主干变红等出事场景也在这里演练。

真实项目（agent-relay、module-crew 等）仍只开 Plan，不在这里。

演练 3：撤回 #7 后，autopilot 会开降级 issue，并在下次运行时收窄 drill-div 的接管档位。
