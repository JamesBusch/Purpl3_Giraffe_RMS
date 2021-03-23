import './run_script_page.css';
import axios from "axios";
import Table from '../table/table_soory.js';
import LiveOutput from './LiveOutput.js';

const RunScriptPage = (props) => {
    return (
        <div>
            <div className="body">
                <div className="column">
                    <h1>Select Computer</h1>
                    <div className="scroll">
                        <Table input={[{name:'soory\'s computer\tIp:123.1234.7777',script:Select_computer_func},{name:'tom\'s computer     Ip:123.1234.7777',script:Select_computer_func},{name:'jeary\'s computer     Ip:123.1234.7777',script:Select_computer_func}]}/>
                    </div>
                </div>

                <div className="column">
                    <h1>Select Script</h1>
                    <div className="scroll">
                        <Table input={[{name:'script_1',script:Select_script_func},{name:'diamond hands script',script:Select_script_func},{name:'monkey see monkey do',script:Select_script_func}]}/>
                    </div>
                </div>

                <p id="Select_Computer_text"></p>
                <p id="Select_Script_text"></p>
            </div>

            <footer>
                <div className="Run_Button">
                    <button type="button" onClick={Run_script}>Run Script</button>
                </div>

                <button type="button" onClick={Update}>Test on main page</button>
                <LiveOutput test={5}/>
            </footer>
        </div>
    )
}

function Update() {
    let scriptID = document.getElementById("Select_Script_text").value;
    alert(scriptID);
}

function Select_computer_func(parms){
    let text = document.getElementById("Select_Computer_text");
    text.textContent = "Selected Computer : " + parms;
    text.value = parms;
}

function Select_script_func(parms){
    let text = document.getElementById("Select_Script_text");
    text.textContent = "Selected Script : " + parms;
    text.value = parms;
}

function Run_script(parms){
    let in_computer = document.getElementById("Select_Computer_text");
    let in_script = document.getElementById("Select_Script_text");

    axios.post("/api", {
        body: {
          op:"RUN_SCRIPT",
          data:{
            ScriptID: in_script.value,
            ComputerID: in_computer.value
          }
        }
        }).then((res) => {
          alert(JSON.stringify(res.data))
          let btn = document.getElementById("run_page_runbtn");
          btn.value = res.data;
          console.log(btn.value.Id);
        }).catch((res) =>{
          alert("Post Failed")
        })
}
  

export default RunScriptPage
