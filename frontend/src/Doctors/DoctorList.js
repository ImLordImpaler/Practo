import React from 'react';
import {Button} from 'reactstrap';

class DoctorList extends React.Component{
    constructor(props){
        super(props);
        
        this.fetchDocs = this.fetchDocs.bind(this)
    }
    fetchDocs(){
        fetch('http://127.0.0.1:8000/users/')
        .then(response => response.json())
        .then(data =>
            console.log('Data:' , data)
            )
    }
    render(){
        return(
            <div className='container'>
                    <Button onClick = {this.fetchDocs}>Fetch!</Button>
            </div>
        );
    };
}

export default DoctorList;