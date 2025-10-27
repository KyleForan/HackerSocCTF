# Janky setup but it works
# gcc <input.c> -o <output> -no-pie -m32 -w;
for file in ./*/*;
do
    if [[ "$file" == *.c ]] then
        echo $file;

        outputname=${file%.c}
        outputname="${outputname//src/level}"

        echo "Compiling $file into $outputname"

        gcc $file -o $outputname -no-pie -m32 -w;
        chmod +x $outputname
    fi
done