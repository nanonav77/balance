const express = require('express')
const app = express()
const path = require('path') 

// Configuración de la aplicación
app.set('port',7000);

// Middlewares para la navegación de archivos y carpetas
app.use(express.static(path.join(__dirname,'public')))


// Declaramos la rutas que van a redirigir la aplicación
app.get('/', (req, res) => {

    res.send('Bienvenidos a Balance');

})

app.listen(app.get('port'), () => {

    console.log('Aplicación corriendo en el puerto: '+app.get('port') );

})