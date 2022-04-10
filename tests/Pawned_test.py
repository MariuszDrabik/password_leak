import pytest
from modules.Exceptions import LengthException, LetterException, NumberException, SpecialCharException
from modules.PasswdValidator import PasswdValidator


def test_checks():
    password = '12345As@'
    password_1 = 'aaaaaaaaAs@'
    password_2 = '1233245A@'
    password_3 = '12dsf345s@'
    password_4 = '12dsf345sA'
    password_5 = 'As%1'
    
    validator = PasswdValidator(password)
    validator_1 = PasswdValidator(password_1)
    validator_2 = PasswdValidator(password_2)
    validator_3 = PasswdValidator(password_3)
    validator_4 = PasswdValidator(password_4)
    validator_5 = PasswdValidator(password_5)
    
    with pytest.raises(NumberException) as exc_1:
        validator_1.validate()        
    
    with pytest.raises(LetterException) as exc_2:
        validator_2.validate()
    
    with pytest.raises(LetterException) as exc_3:
        validator_3.validate()
    
    with pytest.raises(SpecialCharException) as exc_4:
        validator_4.validate()
        
    with pytest.raises(LengthException) as exc_5:
        validator_5.validate()    
            
    assert validator.validate() is True
    
    assert str(exc_1.value) == 'Password has not any number'
    
    assert str(exc_2.value) == 'Password has not any lower letter'
    
    assert str(exc_3.value) == 'Password has not any capital letter'
    
    assert str(exc_4.value) == 'Password has not any special character'
        
    assert str(exc_5.value) == 'Password is too short'