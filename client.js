async function fetchCityData(cityName) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/weather/?city_name=${encodeURIComponent(cityName)}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

// let p1=fetchCityData('Tashkent').then(data => {
//     console.log('Fetched data:', data);
// }).catch(error => {
//     console.error('Error in fetchCityData:', error);
// });

// let p2=fetchCityData('Samarkand').then(data => {
//     console.log('Fetched data:', data);
// }).catch(error => {
//     console.error('Error in fetchCityData:', error);
// });

// console.log('Fetching data for Tashkent and Samarkand...');
// console.log('p1:', p1);
// console.log('p2:', p2); 
// console.log('All fetch operations initiated.');

console.log('waiting Samarkand data until Tashkent data is fetched and showed...');
let p1=fetchCityData('Tashkent').then(data => {
    console.log('Fetched data:', data);
}).catch(error => {
    console.error('Error in fetchCityData:', error);
});
console.log('p1:', p1);
let p2=p1.then(data => {
    return fetchCityData('Samarkand');
}).catch(error => {
    console.error('Error in fetchCityData for Tashkent:', error);
});

p2.then(data => {
    console.log('Fetched data:', data);
}).catch(error => {
    console.error('Error in fetchCityData for Samarkand:', error);
});

console.log('All fetch operations initiated.');