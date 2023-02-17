function compareJSON(obj1, obj2) {
  let result = {};
  for (let key in obj1) {
    if (obj1.hasOwnProperty(key)) {
      if (obj2.hasOwnProperty(key)) {
        if (obj1[key] !== obj2[key]) {
          result[key] = { "obj1": obj1[key], "obj2": obj2[key] };
        }
      } else {
        result[key] = { "obj1": obj1[key], "obj2": null };
      }
    }
  }
  for (let key in obj2) {
    if (obj2.hasOwnProperty(key)) {
      if (!obj1.hasOwnProperty(key)) {
        result[key] = { "obj1": null, "obj2": obj2[key] };
      }
    }
  }
  return result;
}

let obj1 = { "name": "John", "age": 30, "city": "New York" };
let obj2 = { "name": "John", "age": 35, "city": "Chicago" };

console.log(compareJSON(obj1, obj2)); // output: { "age": { "obj1": 30, "obj2": 35 }, "city": { "obj1": "New York", "obj2": "Chicago" } }
