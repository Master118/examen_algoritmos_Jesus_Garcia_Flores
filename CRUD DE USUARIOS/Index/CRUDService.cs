public bool Deleteusers(int idusuario)
        {
            respuesta = wsSegumientoPret.Deleteusers(idusuario);      
            return respuesta;
        }