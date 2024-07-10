int minOperations(char** logs, int logsize){
    int beg = 0;
    int cur = 0;
    for (int i = 0; i < logsize;  i++)
    {
        printf("%s\n", logs[i]);
        if ((strcmp(logs[i], "../") == 0 && cur == 0) || strcmp(logs[i], "./") == 0){
            continue;
        }
        if (strcmp(logs[i], "../") == 0 && cur != 0){
            cur--;
        }
        else{
            cur++;
        }
    }
    return cur - beg;
}