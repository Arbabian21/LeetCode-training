# You can insert into a linked list
    # at the beginning of the linked list
    # after a node in the linked list
    # at the end of the linked lsit
    
# inserting into the beginning of a list
    # create your new node
    # have your new node point to the current head of the liniked list
    # havee the head of your linked list point to your new node
    
# inserting after a random node in the linked list
    # create your new node
    # traverse your linked list till you get to the node you want to put the new node after
    # set the 'next' node memory location of your new node, equal to the 'next' node your current node alraedy points to
    # make the current nodes 'next' node memory location point to the memory locatiuon of the new node you made

# inserting to the end of a linked list
    # create your new node
    # traverse the linked list till you get to a node that has 'next' equal to "None" signifiygin that this is the last node
    # set the currNodes 'next' equal to your newNodes memory location. 
    # makew sure newNodes 'next' is equal to None
    # make tail point to your newNode