#include <iostream>

using namespace std;

/**
 * Class representing a node in a binary tree.
 */
class Node {
    int key; // The value of the node.
    Node *left; // Pointer to the left child.
    Node *right; // Pointer to the right child.

public:
    /**
     * Constructor initializes a node with default values.
     */
    Node() {
        key = -1;
        left = nullptr;
        right = nullptr;
    };

    // Setters and getters for the node's properties.
    void setKey(int aKey) { key = aKey; }
    void setLeft(Node *aLeft) { left = aLeft; }
    void setRight(Node *aRight) { right = aRight; }
    int Key() { return key; };
    Node *Left() { return left; };
    Node *Right() { return right; };

};

/**
 * Class representing a binary tree.
 */
class Tree {
    Node *root; // Pointer to the root node of the tree.

public:
    Tree(); // Constructor
    ~Tree(); // Destructor

    // Getter for the root node.
    Node *Root() { return root; };

    // Public interface for adding nodes to the tree.
    void addNode(int key);

    // Tree traversal functions.
    void inOrder(Node *n);
    void preOrder(Node *n);
    void postOrder(Node *n);

private:
    // Helper functions for adding nodes and freeing memory.
    void addNode(int key, Node *leaf);
    void freeNode(Node *leaf);
};

// Implementation of Tree's public and private member functions.

Tree::Tree() { root = nullptr; } // Constructor initializes the tree with no root.

Tree::~Tree() { freeNode(root); } // Destructor frees all nodes starting from the root.

/**
 * Recursively frees memory allocated for nodes.
 * @param leaf The current node being freed.
 */
void Tree::freeNode(Node *leaf) {
    if (leaf != nullptr) {
        freeNode(leaf->Left());
        freeNode(leaf->Right());
        delete leaf;
    }
}

/**
 * Adds a node with the given key to the tree.
 * If the tree is empty, the new node becomes the root.
 * Otherwise, calls the private addNode to place the node correctly.
 * @param key The value of the new node.
 */
void Tree::addNode(int key) {
    if (root == nullptr) {
        cout << "add root node ..." << key << endl;
        Node *n = new Node();
        n->setKey(key);
        root = n;
    } else {
        cout << "add other node ..." << key << endl;
        addNode(key, root);
    }
}

/**
 * Private function to correctly insert a new node in the tree.
 * @param key The value of the new node.
 * @param leaf The current node in the tree during the recursive search for the insertion point.
 */
void Tree::addNode(int key, Node *leaf) {
    if (key <= leaf->Key()) {
        if (leaf->Left() != nullptr)
            addNode(key, leaf->Left());
        else {
            Node *n = new Node();
            n->setKey(key);
            leaf->setLeft(n);
        }
    } else {
        if (leaf->Right() != nullptr)
            addNode(key, leaf->Right());
        else {
            Node *n = new Node();
            n->setKey(key);
            leaf->setRight(n);
        }
    }
}

/**
 * Performs an in-order traversal of the tree and prints each node's key.
 * @param n The current node in the traversal.
 */
void Tree::inOrder(Node *n) {
    if (n) {
        inOrder(n->Left());
        cout << n->Key() << " ";
        inOrder(n->Right());
    }
}

/**
 * Performs a pre-order traversal of the tree and prints each node's key.
 * @param n The current node in the traversal.
 */
void Tree::preOrder(Node *n) {
    if (n) {
        cout << n->Key() << " ";
        preOrder(n->Left());
        preOrder(n->Right());
    }
}

/**
 * Performs a post-order traversal of the tree and prints each node's key.
 * @param n The current node in the traversal.
 */
void Tree::postOrder(Node *n) {
    if (n) {
        postOrder(n->Left());
        postOrder(n->Right());
        cout << n->Key() << " ";
    }
}

int main(){
    // Create a new Tree instance.
    Tree* tree = new Tree();

    // Add nodes to the tree with specific keys.
    tree->addNode(30);
    tree->addNode(10);
    tree->addNode(20);
    tree->addNode(40);

    // Perform and display an in-order traversal of the tree.
    cout << "In order traversal" << endl;
    tree->inOrder(tree->Root());
    cout << endl;

    // Perform and display a pre-order traversal of the tree.
    cout << "Pre order traversal" << endl;
    tree->preOrder(tree->Root());
    cout << endl;

    // Perform and display a post-order traversal of the tree.
    cout << "Post order traversal" << endl;
    tree->postOrder(tree->Root());
    cout << endl;

    // Clean up the dynamically allocated tree to prevent memory leaks.
    delete tree;

    return 0;
}