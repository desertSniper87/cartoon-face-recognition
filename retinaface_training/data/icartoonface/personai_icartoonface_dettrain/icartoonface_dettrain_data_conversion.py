def main():
    with open('./icartoonface_dettrain.csv') as f , open('../train/label.txt', 'w+') as fout:
        for line in f:
            print(line)
            [filename, w, x, y, z] = line.split(',')
            fout.write('# images/' + filename + '\n')
            fout.write(f' '.join(x for x in [w, x, y, z]))

        fout.close()



if __name__ == "__main__":
    main()
