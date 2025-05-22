import axios from 'axios';
import '../styles/OrderForm.css';
import Footer from '../components/Footer.jsx'
import Header from '../components/Header.jsx';
import React, { useEffect, useState } from 'react';
import ErrorBasket from '../components/ErrorBasket.jsx'

const OrderForm = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Функция для загрузки данных о заявках
  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const pk = localStorage.getItem('pk');
        const response = await axios.get('http://localhost:8001/application/', {
          params: {
            pk: pk
          },
        });
        setOrders(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Ошибка при получении данных о заявках:', error);
        setError(error);
        setLoading(false);
      }
    };

    fetchOrders();
  }, []);

  // Функция для форматирования даты
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  // Функция для определения цвета статуса
  const getStatusColor = (order) => {
    if (order.is_active) return '#4CAF50'; // Зеленый
    if (order.is_progress) return '#2196F3'; // Синий
    if (order.is_close) return '#9E9E9E'; // Серый
    if (order.is_draft) return '#FFC107'; // Желтый
    if (order.is_reject) return '#F44336'; // Красный
    return '#000'; // Черный
  };

  // Функция для определения текста статуса
  const getStatusText = (order) => {
    if (order.is_active) return 'Активна';
    if (order.is_progress) return 'В процессе';
    if (order.is_close) return 'Закрыта';
    if (order.is_draft) return 'Черновик';
    if (order.is_reject) return 'Отклонена';
    return 'Неизвестно';
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return (
      <div>
        <Header />
        <ErrorBasket />
        <Footer />
      </div>
    )
  }

  return (
    <div>
      <Header />
      <div className="order-form">
        <h2>ЗАЯВКИ</h2>
        {orders.map((order, index) => (
          <div key={index} className="order-item">
            <div className="order-header">
              <div className="order-id">Заявка #{index + 1}</div>
              <div className="order-status" style={{ backgroundColor: getStatusColor(order) }}>
                {getStatusText(order)}
              </div>
            </div>
            <div className="order-details">
              <div className="order-detail">
                <span className="detail-label">Дата создания:</span>
                <span className="detail-value">{formatDate(order.created_at)}</span>
              </div>
              <div className="order-detail">
                <span className="detail-label">Дата удаления:</span>
                <span className="detail-value">{formatDate(order.deleted_at)}</span>
              </div>
              <div className="order-detail">
                <span className="detail-label">Количество товара:</span>
                <span className="detail-value">{order.quantity_product}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default OrderForm;
