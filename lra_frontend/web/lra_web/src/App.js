import logo from './logo.svg';
import './App.css';
import './style.css';

function App() {
  return (
   <div className="main">
    <div className="section">
    <div className="section-login">
      <form>
        <h2>Login</h2>
        <input type="email" id='email' placeholder="Email"/>
        <input type="password" id='pwd' placeholder="password"/>
        <button className='btn'>Login</button>
      </form>
    </div>
    <div className="section-signup">
      <form>
      <h2>Sign Up</h2>
        <input class="input" type="email" id='email' placeholder="Email"/>
        <input type="password" id='pwd' placeholder="password"/>
        <button className='btn'>Sign Up</button>
      </form>
    </div>
   
    </div>
    
    
   </div>
  );
}

export default App;
