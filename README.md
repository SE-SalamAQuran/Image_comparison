# Task

There are three ways to perform this without having to use a web framework like Django or Flask.

1) Keypoints matching (Slow & may be hard to implement, but robust).
2) Histogram method (Faster & easy to implement, but not robust, may not work for edited/rotated/colored images).
3) Semantic Texton Forests (Fast, Robust, but the hardest to implement).

So I'm gonna trying solving this problem with Semantic Texton Forests, since it's the most efficient way to implement the solution.
Also, STF combines Keypoints matching & decision trees.
