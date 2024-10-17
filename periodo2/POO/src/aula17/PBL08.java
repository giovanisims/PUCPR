package aula17;

public class PBL08 {
}

abstract class SecurityException extends Exception {}

class InvalidBalanceException extends Exception {
    @Override
    public String toString() {
        return "InvalidBalanceException: The balance is insufficient for the requested withdrawal.";
    }
}
abstract class AuthenticationException extends SecurityException {}

class InvalidTimeException extends java.lang.SecurityException {
    @Override
    public String toString() {
        return "InvalidTimeException: The operation is not allowed at this time.";
    }
}

class InvalidAccountException extends AuthenticationException {
    @Override
    public String toString() {
        return "InvalidAccountException: The account number provided is invalid.";
    }
}
class InvalidPasswordException extends AuthenticationException {
    @Override
    public String toString() {
        return "InvalidPasswordException: The password provided is incorrect.";
    }
}