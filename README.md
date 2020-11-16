# Algorithms-TSNE
How are algorithms really related? We use tag data from solved.ac and matrix factorization to find out.

[!img](img.png)

## Introductions

First we collect datas from solved.ac to find problems with tags. Here, by tags we mean algorithms. We use these tags as "items" and problems as "users", and do matrix factoriztion.
We could've used other MF algorithms, but here we just use naive methods with Gradient descent, which is, not ideal but fast to implement and not think about it.
To embedd on my personal blog, I've used bokeh. We also get how other problems are related with other algorithms, but is unused.
Try out this interactive plot here:

https://www.simoryu.com/algo_plot

Entire process is in the repo, so check out if you are interested.
