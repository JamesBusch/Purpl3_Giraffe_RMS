import React, {useState, useEffect} from "react";
import './ScriptForm.css'
import axios from "axios";

const EditScript = (props) => {

    const [name, setName] = useState('')
    const [filename, setFileName] = useState('')
    const [description, setDescription] = useState('')
    const [admin, setAdmin] = useState(false)
    const [data, setdata] = useState('')

    useEffect(() => {
        axios.post("/api", {
            body: {
              op: "MANAGE_SCRIPTS",
              data:{
                funcOP: "GET_BY_ID",
                data: {
                    Id: props.scriptid
                }
              }
            }
            }).then((res) => {
            let entry = res.data.entry;
              alert(JSON.stringify(res.data.entry))
              setDescription(entry.desc);
              setName(entry.name);
              setFileName(entry.filename);
              if((entry.isAdmin).localeCompare("True") == 0){
                setAdmin(true);
              }
              else{
                setAdmin(false);
              }
            }).catch((res) =>{
              alert("Post Failed")
            })
    }, [])

    return (
        <div className="form-popup">
            <div className="form-content">
                <h2>Edit Script</h2>

                <label for="name"><b>Name</b></label><br/>
                <input type="text"name="name" value={name} onChange={(e) => setName(e.target.value)}/><br/><br/>

                <label for="filename"><b>File Name</b></label><br/>
                <input type="text" name="filename" value={filename} onChange={(e) => setFileName(e.target.value)} disabled/><br/><br/>

                <label for="desc"><b>Description</b></label><br/>
                <input type="text" name="desc" value={description} onChange={(e) => setDescription(e.target.value)}/><br/><br/>

                <label for="isAdmin"><b>Admin</b></label>
                <input type="checkbox" value={admin} onChange={(e) => setAdmin(e.currentTarget.checked)}></input><br/>

                <textarea value={data} onChange={(e) => setdata(e.target.value)}>Enter script here...</textarea>
            
                <div className="button-container">
                    <button type="button" onClick={() => props.editScript(props.scriptid, name, filename, description, admin, data)} className="btn">Save</button>
                    <button type="button" className="btn" onClick={() => props.closeForm()} style={{backgroundColor: "#FF6347"}}>Cancel</button>
                </div>
            </div>
        </div>
    )


}

export default EditScript