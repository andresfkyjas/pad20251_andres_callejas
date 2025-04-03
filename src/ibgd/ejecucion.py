from chatgptcliente import ChatGPTClient
from chatsessionDB import ChatSessionDB

if __name__ == "__main__":
    
    ruta_static = "src/ibgd/static/"
    ruta_config = "{}{}".format(ruta_static,"config.json")
    client = ChatGPTClient(ruta_config)
    db = ChatSessionDB('chat_sessions.db')
    
    session_id = "sesion_1"  
    while True:
        pregunta = input("Introduce tu pregunta (o 'exit' para salir): ")
        if pregunta.lower() == "exit" or pregunta.lower() == "salir" or pregunta.lower() == "terminar":
            print("Saliendo del programa...")
            break
        
       
        respuesta = client.send_request(pregunta)
        print("Respuesta:", respuesta)
        
       
        db.log_request(session_id, pregunta, respuesta)
    
   
    db.close()