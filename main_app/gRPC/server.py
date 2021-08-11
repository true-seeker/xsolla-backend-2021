import time
from concurrent import futures

import grpc

import mailer
import proto.mailer_pb2
import proto.mailer_pb2_grpc


class MailerServicer(proto.mailer_pb2_grpc.MailerServicer):
    def send_email(self, request, context):
        response = proto.mailer_pb2.Text()
        response.data = mailer.send_email(request.data)
        return response


def serve():
    # создаем сервер
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    proto.mailer_pb2_grpc.add_MailerServicer_to_server(MailerServicer(), server)
    # запускаемся на порту 6066
    print('Starting server on port 6066.')
    server.add_insecure_port('[::]:6066')
    server.start()

    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
