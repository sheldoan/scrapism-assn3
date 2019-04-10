function search(elem) {
  if(event.key === 'Enter') {
      var search = document.getElementById("search-input").value;
      var displayObject = document.getElementsByClassName('wrapper')[0];
      displayObject.innerHTML = ''

      var results = []
      for (var i = 0; i < data.length; i++) {
        var summary = data[i]['summary']
        if (summary.toLowerCase().includes(search.toLowerCase())) {
          console.log(data[i]['thumb_image_url'])
          results.push(data[i])

          var imageFilename = data[i]['thumb_image_url']
          var coupleImage = document.createElement("img")
          coupleImage.setAttribute('title', data[i]['headline'])
          coupleImage.setAttribute('src', imageFilename)
          displayObject.appendChild(coupleImage)
        }
      }
  }
}
