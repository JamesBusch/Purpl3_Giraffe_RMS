import './table.css'
import Button from './button/button_soory.js';

const Table = (props) => {
    const comp = this;
    console.log(comp);
    return (
        <div id="table">
            {addButtons(props)}
        </div>
    )
}
function addButtons(params) {
    console.log(params);
    let output = params.input.map(item=> <Button name={item.name} func={item.script}/>)
    
    return <div>{output}</div>
}

export default Table
