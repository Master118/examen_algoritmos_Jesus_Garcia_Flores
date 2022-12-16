 $scope.borrarUsuario = function () {
            $http.get('/CRUD/borrarUsuario?idusuario=' + $scope.idusuario.toString()
                    ).success(function (datainfoSolicitud) {
                        debugger;
                        if (datainfoSolicitud) {
							 $scope.openToast('Se elimino de manera correcta');
                        }
                        else {
                            $scope.openToast('Error al eliminar');
                        }
                    });
            
        };
