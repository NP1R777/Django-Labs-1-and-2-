import '../styles/login.css';
import React, { useState } from 'react';
import Header from '../components/Header.jsx';
import Footer from '../components/Footer.jsx';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { login } from '../redux/actions/authActions.js';

const Login = ({ setUserName }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { loading } = useSelector((state) => state.auth);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      // Диспатчим экшен и ждем его выполнения
      const result = await dispatch(login({ email, password }));

      // Проверяем, что результат успешный
      if (result.error) {
        throw new Error(result.error.message || 'Ошибка аутентификации');
      }

      // Перенаправляем на главную страницу
      navigate('/');

      // Показываем всплывающее окно
      alert('Вы успешно авторизировались!');
    } catch (error) {
      console.error('Ошибка при входе:', error);
      setError(error.message || 'Произошла ошибка при входе. Пожалуйста, попробуйте позже.');
    } finally {
      setIsLoading(false);
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div>
      <Header />
      <div className="login-container">
        <div className="login-card">
          <h2 className="login-title">Войти</h2>
          {error && <div className="error-message">{error}</div>}
          <form onSubmit={handleSubmit} className="login-form">
            <div className="form-group">
              <label htmlFor="email" className="form-label">Email/номер телефона:</label>
              <input
                type="text"
                id="email"
                className="form-input"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                disabled={isLoading || loading}
                placeholder="Введите email или номер телефона"
              />
            </div>
            <div className="form-group">
              <label htmlFor="password" className="form-label">Пароль:</label>
              <div className="password-input-container">
                <input
                  type={showPassword ? "text" : "password"}
                  id="password"
                  className="form-input"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  disabled={isLoading || loading}
                  placeholder="Введите пароль"
                />
                <button
                  type="button"
                  className="password-toggle"
                  onClick={togglePasswordVisibility}
                >
                  {showPassword ? 'Скрыть' : 'Показать'}
                </button>
              </div>
            </div>

            <button
              type="submit"
              className="login-button"
              disabled={isLoading || loading}
            >
              {isLoading || loading ? (
                <>
                  <span className="spinner"></span>
                  Вход...
                </>
              ) : (
                'Войти'
              )}
            </button>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Login;
