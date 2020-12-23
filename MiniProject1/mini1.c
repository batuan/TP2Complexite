#include "MiniProject1.h"

int main(int argc, char const *argv[])
{
    /* code */
    if(argc != 3) {
        printf("error: for using type: \n./mini1 dimacs.txt affectation.txt\n");
        return 0;
    }

    char * problemPath = argv[1];
    char * affectationPath = argv[2];

    struct SATProblem problem =
            readSATProblem(problemPath);
    int varialbes = problem.variables;
    struct Affectation affec =
            readAffectation(affectationPath, varialbes);

    time_t begin = clock();
    printf("verify: %d\n", verifySAT(problem, affec));
    double time_spent = 0.0;
    time_spent += (double)(clock() - begin) / CLOCKS_PER_SEC;
    printf("Time for verify dimacs cnf: %f (seconds) \n", time_spent);
    return 0;
}