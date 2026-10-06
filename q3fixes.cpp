class ListItem {
    public:
        ListItem *next;
        ListItem *prev;
        int id;
        char name[9];
};
class UserList {
    public:
        ListItem *head;
        void insert(char *, int);
        void deleteByName(char *);
        int idForName(char *);
};
void UserList::insert(char *name, int id) {
    // Fix for mistake #1
    if (this->head == NULL) {
        return;
    }
    // Fix for Mistake #4
    if (id < 0) {
        perror("Id must be positive");
    }
    ListItem *user = new ListItem();
    user->id = id;
    // Fix for Mistake #3
    strncpy(user->name, name);
    user->next = this->head;
    this->head->prev = user;
    this->head = user;
}
void UserList::deleteByName(char *name) {
    // Fix for mistake #1
    if (this->head == NULL) {
        return;
    }
    ListItem *curr = this->head;
    ListItem *next = curr->next;
    while (curr != NULL) {
        if (strcmp(curr->name,name)==0) {
            // Fix for mistake #2
            if (curr->prev != NULL) {
                curr->prev->next = next;
                next->prev = curr->prev;
            } else {
                curr->next->prev = NULL;
            }
            delete curr;
            return;
        }
        curr = next;
        next = next->next;
    }
}
int UserList::idForName(char *name) {
    ListItem *curr = this->head;
    while (curr != NULL) {
        if(strcmp(curr->name,name) == 0) {
            return curr->id;
        }
    }
    return -1;
}