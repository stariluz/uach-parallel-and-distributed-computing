import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

# Clase para representar una cuenta bancaria
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.semaphore = threading.Semaphore(2)  # Semáforo para controlar el acceso a la cuenta

    # Método para depositar dinero en la cuenta
    def deposit(self, amount):
        with self.semaphore:  # Controla el acceso a la cuenta con un semáforo
            self.balance += amount
            logging.info(f'Deposit of {amount}. Current balance: {self.balance}')

    # Método para retirar dinero de la cuenta
    def withdraw(self, amount):
        with self.semaphore:  # Controla el acceso a la cuenta con un semáforo
            if self.balance >= amount:
                self.balance -= amount
                logging.info(f'Withdrawal of {amount}. Current balance: {self.balance}')
            else:
                logging.warning(f'Failed withdrawal. Insufficient balance: {self.balance}')

# Función para simular múltiples depósitos
def perform_deposits(account, amount, times):
    for _ in range(times):
        account.deposit(amount)

# Función para simular múltiples retiros
def perform_withdrawals(account, amount, times):
    for _ in range(times):
        account.withdraw(amount)

if __name__ == '__main__':
    # Crear una cuenta bancaria con un saldo inicial de 300
    account = BankAccount(initial_balance=300)

    # Crear hilos para realizar depósitos y retiros
    deposit_thread = threading.Thread(target=perform_deposits, args=(account, 50, 100))
    withdrawal_thread = threading.Thread(target=perform_withdrawals, args=(account, 50, 100))

    # Iniciar los hilos
    deposit_thread.start()
    withdrawal_thread.start()

    # Esperar a que los hilos terminen
    deposit_thread.join()
    withdrawal_thread.join()

    # Imprimir el saldo final de la cuenta
    logging.info(f'Final account balance: {account.balance}')
