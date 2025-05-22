import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/NotFound.css'

const NotFound = () => {
  const navigate = useNavigate();

  const handleRegister = () => {
    navigate('/register');
  };

  const handleLogin = () => {
    navigate('/login');
  };

  return (
    <div className="not-found-container">
      <div className="not-found-content">
        <div className="not-found-header">
          <h1 className="not-found-title">404</h1>
          <p className="not-found-message">
            Пока корзина недоступна.
            <p className='article-new'>
              Нажмите на кнопку для регистрации,
              или войдите, если у Вас есть аккаунт!
            </p>
          </p>
        </div>
        <button
          className="register-button1"
          onClick={handleRegister}
        >
          Зарегистрироваться!
        </button>
        <p>
          <button
            className='login-button1'
            onClick={handleLogin}
          >
            Войдите, если есть аккаунт!
          </button>
        </p>
      </div>
    </div>
  );
};

export default NotFound;
