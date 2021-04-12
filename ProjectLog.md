### Motivation

Project reading log.

1. Read dataset collection code -> scripted task in PyBullet, I know it fairly well (in gym style).
2. Train policy in server -> see how much time it takes to train the network.
3. Run evaluate code to see how to use the model (in gym style).
4. See task environment observation in detail.

### Observation

I may pay attention to the hyper-parameter tuning, this may not be as harsh as the benchmarks in computer vision.

I observe that some standard camera would have some fixed intrinsics.

I realize that Andy Zeng has done what I was trying to do fairly well. I think this means that I should be agile to do
good AI.

I realize that there's full of unknown in AI research.

I observe that block insertion works pretty well after just a little training.

Andy Zeng implements pick-place and push, and I realize that this is pretty simple. Previously, without enough
tech-communication, I failed to focus on what is important.

Finally, Let us see the network input-output. We can see that the network ultimately predicts two arguments -> pick pose
and place pose. And the env step is accomplished by these primitives. Then, let's see the models.

I suddenly understand that, I would build on this project to construct a rearrangement task. 
Since we have a goal-conditioned ravens here. 