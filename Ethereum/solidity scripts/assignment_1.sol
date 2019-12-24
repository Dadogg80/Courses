pragma solidity 0.5.12;
// updated from 0.5.1 to 0.5.12 compiler


contract MemoryAndStorage {

    mapping(uint => User) private users;
    // Creates an mapping the key is a number and the value is User, mapping is private and is named users

    struct User {
    // Creates an struct User and contains an id number and a balance
        uint id;
        uint balance;
    }

    function addUser(uint id, uint initialBalance) public {
    // This function add User and takes id and initialBalance as arguments
        users[id] = User(id, initialBalance);
        // this creates an User with an id and initialBalance, then adds it to the users mapping
    }

    function updateBalance(uint id, uint newBalance) public {
        // This function updates the balance of the id to the newBalance argument
        users[id].balance = newBalance;
    }

    function getBalance(uint id) public view returns(uint) {
        // This function returns the stored value(balance) in the users mapping of the given id argument
        return users[id].balance;
    }

}
