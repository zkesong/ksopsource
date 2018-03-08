namespace java HelloThrift.Interface

service HelloService{

    string HelloString(1:string para)

    i32 HelloInt(1:i32 para)

    bool HelloBoolean(1:bool para)

    void HelloVoid()

    string HelloNull()

}