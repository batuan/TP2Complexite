//
// Created by Ba Tuan on 19/12/2020.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include<unistd.h>
char mm[255];
char *preamble = NULL;
int count = 0;
int square = 0;
int count1 = 0;
int encode(int row, int col, int digit) {
    return square*square*(row-1) + square * (col-1) + digit;
}

void preAssign(char * filename, int size) {
    //char path[100] = "../TestData/sudoku/";
    //strcat(path, filename);
    FILE *filepre = fopen(filename, "r");
    if (filepre == NULL) {
        fprintf(stderr,"Error in creating %s: aborting.\n", filename);
        exit(-1);
    }

    int i = 0;
    int x = 1;
    int y = 1;
    //printf("Pre-assign: ");
    fscanf (filepre, "%d", &i);
    count1++;
    while (!feof (filepre))
    {
        if(i!=0) {
            count1++;
            sprintf(mm, "%d 0\n", encode(x, y, i));
            count ++;
            strcat(preamble, mm);
        }
        fscanf (filepre, "%d", &i);
        y+=1;
        if(y==size+1) {
            x+=1;
            y=1;
        }
    }
    fclose(filepre);
    //printf("%s", preamble);
}

int main(int argc, char const *argv[])
{
    /* code */
    if( argc != 3 ) {
        printf("error: for using, type: \n./mini3 sudosufile.txt k\n");
        return 0;
    }
    char filename[100];
    strcpy(filename, argv[1]);
    int size = atoi(argv[2]);
    square = size * size;
    preamble = (char *)calloc(80000, sizeof(char));
    clock_t begin = clock();
    //pre-assign
    preAssign(filename, square);
    //write to file
    char path[100] = "../TestData/sudoku2sat/";
    char *ptr = strtok(filename, "./");
    ptr = strtok(NULL, "./");
    ptr = strtok(NULL, "./");
    strcat(path, ptr);
    char path1[100];
    strcpy(path1, path);
    strcat(path1, "clone.txt");
    strcat(path, "_2CNF.txt");
    FILE *file = fopen(path1, "w");
    if (file == NULL) {
        fprintf(stderr,"Error in creating %s: aborting.\n", path1);
        exit(-1);
    }

    fprintf(file, "%s", preamble);

    // 1; There is at least one number in each entry

    for(int x = 1; x <= square; x++) {
        for(int y = 1; y <= square; y++) {
            for(int z = 1; z <= square; z++) {
                fprintf(file, "%d ", encode(x, y, z));
                //strcat(preamble, mm);
            }
            //strcat(preamble, "0\n");
            fprintf(file, "0\n");
            count ++;
        }
    }

    //2 Each number appears at most once in each row:
    // s(xyz) -> - s((x+1)yz); s(xyz) -> -s((x+2)yz;...
    for(int y = 1; y <= square; y++) {
        for(int z = 1; z <= square; z++) {
            for(int x = 1; x <= square-1; x++) {
                for(int i = x+1; i<=square; i++) {
                    fprintf(file, "%d %d 0\n", -encode(x, y, z), -encode(i, y, z));
                    //strcat(preamble, mm);
                    count ++;
                }
            }
        }
    }
    //3 Each number appears at most once in each column:
    // s(xyz) -> -s(x(y+1)z); s(xyz) -> -s(x(y+2)z;...
    for(int x = 1; x<=square; x++) {
        for (int z = 1; z <= square; z++) {
            for (int y = 1; y <= square-1; y++) {
                for (int i = y+1; i <= square; i++) {
                    fprintf(file, "%d %d 0\n", -encode(x, y, z), -encode(x, i, z));
                    //strcat(preamble, mm);
                    count ++;
                }
            }
        }
    }

    //4 Each number appears at most once in each 3x3 sub-grid:
    //
    for (int z = 1; z <= square; z++) {
        for (int i = 0; i <= size-1; i++) {
            for (int j = 0; j <= size-1; ++j) {
                for (int x = 1; x <= size ; x++) {
                    for (int y = 1; y <= size; y++) {
                        for (int k = y+1; k <= size; k++) {
                            fprintf(file, "%d %d 0\n", -encode(size*i+x, size*j+y, z), -encode(size*i+x,size*j+k, z));
                            //strcat(preamble, mm);
                            count ++;
                        }
                    }
                }
            }
        }
    }

    for (int z = 1; z <= square; z++) {
        for (int i = 0; i <= size-1; i++) {
            for (int j = 0; j <= size-1; ++j) {
                for (int x = 1; x <= size; x++) {
                    for (int y = 1; y <= size; y++) {
                        for (int k = x+1; k <= size; k++) {
                            for (int l = 1; l <= size; l++) {
                                fprintf(file, "%d %d 0\n", -encode(size*i+x, size*j+y, z), -encode(size*i+k,size*j+l, z));
                                //strcat(preamble, mm);
                                count ++;
                            }
                        }
                    }
                }
            }
        }
    }
    fclose(file);
    double time_spent = 0.0;
    time_spent += (double)(clock() - begin) / CLOCKS_PER_SEC;
    //head
    char head[255];
    sprintf(head, "p cnf %d %d\n", square*square*square, count);
    file = fopen(path1, "r");
    FILE *fileSave = fopen(path, "w");
    fprintf(fileSave,"%s", head);
    char c;
    char * line = NULL;
    size_t len = 0;
    // while ((c = getc(file)) != EOF) {
    //     putc(c, fileSave);
    // }
    while(getline(&line, &len, file)!=-1) {
        fprintf(fileSave, "%s", line);
    }
    fclose(file);
    fclose(fileSave);
    remove(path1);
    printf("total pre-assign: %d\n", count1);
    printf("total line: = %d\n", count);
    printf("Time for redution sudoku to Dimacs is %f seconds \n", time_spent);
    return 0;
}
