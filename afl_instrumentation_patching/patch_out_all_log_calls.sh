cp $1 $1.patched
for line in $(objdump -d a.out | grep -P '\<__afl_maybe_log\>$' | awk '{print $1}')
do
    addr=$(printf '%d' 0x$(echo $line | head --bytes=-2))
    for i in 0 1 2 3 4
    do
        printf '\x90' | dd of=$1.patched bs=1 seek=$(($addr + $i)) count=5 conv=notrunc
    done
done
