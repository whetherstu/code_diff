
### Requirements:

* tensorflow (2.0 > tensorflow version >= 1.14.0)
* gensim
* angr
* networkx
* lapjv




```
python3 src/deepbindiff.py --input1 path_to_the_first_binary --input2 /path_to_the_second_binary --outputDir output/
```

* For example, to compare O0 and O1 chroot binaries from coreutils v5.93, you may run:

```
python3 src/deepbindiff.py --input1 /home/DeepBinDiff/experiment_data/coreutils/binaries/coreutils-5.93-O0/chroot --input2 /home/DeepBinDiff/experiment_data/coreutils/binaries/coreutils-5.93-O1/chroot --outputDir output/
```


