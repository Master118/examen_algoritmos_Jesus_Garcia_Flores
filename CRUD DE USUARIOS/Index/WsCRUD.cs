        public DataTable Deleteusers(int idusuario)
        {
            DataSet ds = new DataSet();
            string conn = ActivaPret;
            SqlConnection connection = new SqlConnection();
            connection.ConnectionString = conn;
            string res = string.Empty;
            string strSQL = "EXEC StpD_EliminausuariobyId " + idusuario.ToString()";
            try
            {
                connection.Open();
                SqlCommand cmd = new SqlCommand();
                SqlDataAdapter adapter = new SqlDataAdapter();
                adapter.SelectCommand = new SqlCommand(strSQL, connection);
                adapter.Fill(ds);
                adapter.Dispose();
                adapter = null;
                connection.Close();
            }

            catch (Exception ex)
            {
                res = ex.Message;
            }

            return ds.Tables[0];
        }
