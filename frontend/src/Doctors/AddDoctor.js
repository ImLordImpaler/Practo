import React from 'react';
import {Form , Label , Input , FormGroup , Button} from 'reactstrap';
class AddDoctor extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            id : '',
            firstName : '',
            lastName : '',
            age : '',
            category : '-',

        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleSubmit = event => {

        event.preventDefault();
        const url = 'http://127.0.0.1:8000/users/addDoctor'
        const data =  {firstName  : this.state.firstName , lastName : this.state.lastName}

        fetch(url , {
            method: "POST",
            body: JSON.stringify(data),
            headers: {'Content-Type' : 'application/json'} 
        })
        .then(resp => resp.json())
        .catch(error =>console.log(error))
        .then(respon => 
            console.log('Status:' , respon))
    }
    handleChange = event => {
        
        this.setState({ [event.target.name]:event.target.value })
    }
    render(){
        return(
            <div className='container'>
                    <Form onSubmit = {this.handleSubmit}>
                    <FormGroup>
                        <Label for="exampleName">First Name</Label>
                        <Input type="name" name="firstName" value = {this.state.firstName} onChange = {this.handleChange} placeholder="First Name" />
                    </FormGroup>
                    <FormGroup>
                        <Label for="exampleName">Last Name</Label>
                        <Input type="name" name="lastName" value = {this.state.lastName} onChange = {this.handleChange} id="exampleEmail" placeholder="Last Name" />
                    </FormGroup>
                    <Button type='submit'>Submit</Button>
                    </Form>
            </div>
        );
    };
}

export default AddDoctor;