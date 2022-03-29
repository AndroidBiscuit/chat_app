import { useState } from 'react';
import { sendMessage, isTyping } from 'react-chat-engine';
import { SendOutlined, PictureOutlined } from '@ant-design/icons';


const MessageForm = (props) => {
    const [value, setValue] = useState('');
    const { chatId, creds } = props;

    const handleSubmit = (event) => {
        
        // IMPORTANT - Prevent browser refresh
        event.preventDefault();

        const text = value.trim();

        // Check if textbox is empty (we do not want to send an empty message)
        if (text.length > 0) sendMessage(creds, chatId, {text})

        // Reset value of textbox after sending message
        setValue('');
    };

    // Check if user is typing
    const handleChange = (event) => {
        setValue(event.target.value);

        isTyping(props, chatId);
    };

    // For uploading images
    const handleUpload = (event) => {
        sendMessage(creds, chatId, {files: event.target.files, text: ""})
    };

  return (
    <form className="message-form" onSubmit={handleSubmit}>      
        
        <input comment="Input text for the user"
            className="message-input"
            placeholder="Send a message..."
            value={value}
            onChange={handleChange}
            onSubmit={handleSubmit}
        />

        <label comment="Add an image (button and icon)" htmlFor="upload-button">
            <span className="image-button">
                <PictureOutlined className="picture-icon"/>
            </span>
        </label>

        <input comment="Add an image (upload action)" type="file" multiple={false} id="upload-button" style={{display: 'none'}} onChange={handleUpload}/>

        <button comment="Submit button" type="submit" className="send-button">
            <SendOutlined className="send-icon"/>
        </button>
    </form>
  );
};

export default MessageForm;