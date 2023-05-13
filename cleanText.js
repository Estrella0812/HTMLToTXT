
// function convertToText(html){
//   console.log(html)
//   const { convert } = require('html-to-text');
//   // There is also an alias to `convert` called `htmlToText`.
  
//   const options = {
//     wordwrap: 130,
//   };

//   const text = convert(html, options);
//   console.log(text);
// }




// function convertToText(ye){
//   const { convert } = require('html-to-text');

//   const html = `
//   <div> HELLO WORLD </div>
//   `;


//   const text = convert(html, {
//     wordwrap: 130
//   });
//   console.log(text);
// }

  const fs = require('fs')

  fs.readFile('raw_html.txt', 'utf-8', (err, data) => {
    if (err) throw err;
  
    const { convert } = require('html-to-text');
  
  
    const text = convert(data, {
      wordwrap: 130
    });
    console.log(text);


    fs.writeFile('text.txt', text, err => {
      if (err) throw err;
      // file written successfully
    });
  });



