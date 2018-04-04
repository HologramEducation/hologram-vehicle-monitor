var obd2 = require("obd2");
var OBD = new obd2({
  device  : "ELM327", // Device type
  serial  : "usb",   // usb, bluetooth
  port    : "/dev/tty.wchusbserial141240",   // Device COM port / path
  baud    : 38400,    // Device baud rate
  delay   : 50,       // Ticker delay time (ms)
  cleaner : true      // Automatic ticker list cleaner ( ex. PID not supported, no response )
});

OBD.start( function()
{
  console.log("OBD2 example start");

  OBD.listDTC();

  OBD.on("dataParsed", function( type, elem, data )
  {
    console.log('obd2', type, elem, data );
  });

  OBD.on("pid", function( data )
  {
    console.log('pid', data );
  });

  OBD.on("dtc", function( data )
  {
    console.log('dtcList', data );
  });
});
