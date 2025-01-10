import Lessons from "./Components/Lessons";
import Comment from "./Components/MessageBoard";
import Resource from "./Components/Resource";
import Sound from "./Components/Sound";
import Video from "./Components/Video";
import Quotes from "./Components/QuoteModal";


function App() {
  return (
    <>
    <div>
      <Lessons />
    </div>
    <div>
      <Comment />
    </div>
    <div>
      <Resource />
    </div>
    <div>
      <Sound />
    </div>
    <div>
      <Video />
    </div>
    <div>
      <Quotes />
    </div>
    </>
  )
}

export default App;
