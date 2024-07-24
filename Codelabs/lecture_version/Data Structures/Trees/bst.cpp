#include <iostream>

using namespace std;

// Node class represents a single node in a Binary Search Tree (BST).
class Node {
public:
    int key; // Key value of the node.
    Node *left; // Pointer to the left child.
    Node *right; // Pointer to the right child.

    // Constructor initializes a node with a given key value and null children.
    Node(int value) : key(value), left(nullptr), right(nullptr) {}
};

// BST class represents a Binary Search Tree.
class BST {
private:
    Node *root; // Root node of the BST.

    // Private method to insert a new node with a given key into the BST.
    Node *insert(Node *node, int key) {
        if (node == nullptr) {
            return new Node(key);
        }
        if (key < node->key) {
            node->left = insert(node->left, key);
        } else if (key > node->key) {
            node->right = insert(node->right, key);
        }
        return node;
    }

    // Private method to delete a node with a given key from the BST.
    Node *deleteNode(Node *root, int key) {
        if (root == nullptr) return root;

        if (key < root->key) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->key) {
            root->right = deleteNode(root->right, key);
        } else {
            if (root->left == nullptr) {
                Node *temp = root->right;
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                Node *temp = root->left;
                delete root;
                return temp;
            }

            Node *temp = maxValueNode(root->left); // Find the largest in the left subtree
            root->key = temp->key; // Copy the in-order predecessor's content to this node
            root->left = deleteNode(root->left, temp->key); // Delete the in-order predecessor
        }
        return root;
    }

// Helper function to find the node with the maximum key value in a subtree
    Node *maxValueNode(Node *node) {
        Node *current = node;
        while (current->right != nullptr) {
            current = current->right;
        }
        return current;
    }

    // Private method for in-order traversal of the BST.
    void inOrderTraversal(Node *node) {
        if (node != nullptr) {
            inOrderTraversal(node->left);
            cout << node->key << " ";
            inOrderTraversal(node->right);
        }
    }

    // Private method for pre-order traversal of the BST.
    void preOrderTraversal(Node *node) {
        if (node != nullptr) {
            cout << node->key << " ";
            preOrderTraversal(node->left);
            preOrderTraversal(node->right);
        }
    }

    // Private method for post-order traversal of the BST.
    void postOrderTraversal(Node *node) {
        if (node != nullptr) {
            postOrderTraversal(node->left);
            postOrderTraversal(node->right);
            cout << node->key << " ";
        }
    }

public:
    // Constructor initializes an empty BST.
    BST() {
        root = nullptr;
    }

    // Public method to insert a new key into the BST.
    void insert(int key) {
        root = insert(root, key);
    }

    // Public method to delete a key from the BST.
    void deleteKey(int key) {
        root = deleteNode(root, key);
    }

    // Public method for in-order traversal of the BST.
    void inOrder() {
        inOrderTraversal(root);
        cout << endl;
    }

    // Public method for pre-order traversal of the BST.
    void preOrder() {
        preOrderTraversal(root);
        cout << endl;
    }

    // Public method for post-order traversal of the BST.
    void postOrder() {
        postOrderTraversal(root);
        cout << endl;
    }
};

int main() {
    BST tree;
    int element;

    cout << "Enter elements (use -1 to finish): ";

    while (true) {
        cin >> element;
        if (element == -1) {
            break; // Break out of the loop if the sentinel value is entered
        }
        tree.insert(element);
    }

    // Continue with deletion or traversal
    cout << "In-order traversal: ";
    tree.inOrder();

    // Example: Prompt the user for a key to delete
    int deleteElement;
    cout << "Enter the key of the node to delete: ";
    cin >> deleteElement;
    tree.deleteKey(deleteElement);

    cout << "In-order traversal after deletion: ";
    tree.inOrder();
    cout << "Pre-order traversal after deletion: ";
    tree.preOrder();
    cout << "Post-order traversal after deletion: ";
    tree.postOrder();

    return 0;
}