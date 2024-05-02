from abc import ABC, abstractmethod


class Notification(ABC):

    def __init__(self, mensage) -> None:
        self.mensage = mensage

    @abstractmethod
    def send(self, ip: str = None, porta: str = None, celphone_number: str = None) -> bool: ...


class NotificationEmail(Notification):

    def send(self, ip: str = None, porta: str = None, celphone_number: str = None):
        if len(ip) != 11 or ip[:3] != '192':
            print("mensagem não enviada")
            return False
        if porta != '8000':
            print("Porta errada")
            return False
        print(f"enviando mensagem: {self.mensage} via protocolo SMTP para o socket {ip+'/'+porta}")
        return True


class NotificationSMS(Notification):

    def send(self, ip: str = None, porta: str = None, celphone_number: str = None) -> bool:
        if len(celphone_number.strip().replace('-', '').replace('.', '')) != 11:
            print("numerp de telefone nao existe")
            return False
        print(f"{celphone_number} <- enviando notificação:  {self.mensage}\n")
        return True


if __name__ == '__main__':
    email = NotificationEmail("Olá, você foi selecionado(a)...")
    email.send('192.168.1.2', '8000')
    sms = NotificationSMS("Olá, voçê foi selecionado(a)...")
    sms.send(celphone_number='21976788321')
