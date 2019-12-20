pragma solidity 0.5.12;


// All Solidity contracts starts with contract and it´´s name.
contract HelloWorld{
    // Defines a public string variable named message that stores "Hello World" .
    string public message = 'Hello World Again';

    // Defines a 'getter' function that goes to the variable message and returns it´s stored value.
    function getMessage() public view returns(string memory){
        return message;
    }

    // Defines a 'setter' function that takes an argument 'new message' and sets it to the message variable.
    function setMessage(string memory newMessage) public {
        message = newMessage;
    }


}
