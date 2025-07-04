import './App.css'
import { useReactMediaRecorder } from "react-media-recorder";
import { useState } from "react";
import LIGHT_ON from './assets/LIGHT_ON.png'
import LIGHT_OFF from './assets/LIGHT_OFF.png'
import AC_ON from './assets/AC_ON.png'
import AC_OFF from './assets/AC_OFF.png'
import PROJECTOR_ON from './assets/PROJECTOR_ON.png'
import PROJECTOR_OFF from './assets/PROJECTOR_OFF.png'
import CURTAIN_OPEN from './assets/CURTAIN_OPEN.png'
import CURTAIN_CLOSED from './assets/CURTAIN_CLOSED.png'
import REC_ON from './assets/REC_ON.png'
import REC_OFF from './assets/REC_OFF.png'
import axios from "axios";
import { toast, ToastContainer } from "react-toastify";


function App() {
    const { status, startRecording, stopRecording } = useReactMediaRecorder({
        audio: true,
        mediaRecorderOptions: { mimeType: 'audio/wav' },
        onStop: (blobUrl) => onStop(blobUrl)
    });
    const [objects, setObjects] = useState([
        {
            name: 'lâmpada',
            status: false,
            img: {
                true: LIGHT_ON,
                false: LIGHT_OFF
            }
        },
        {
            name: 'ar condicionado',
            status: false,
            img: {
                true: AC_ON,
                false: AC_OFF
            }
        },
        {
            name: 'projetor',
            status: false,
            img: {
                true: PROJECTOR_ON,
                false: PROJECTOR_OFF
            }
        },
        {
            name: 'cortina',
            status: false,
            img: {
                true: CURTAIN_OPEN,
                false: CURTAIN_CLOSED
            }
        },
        {
            name: 'gravação',
            status: false,
            img: {
                true: REC_ON,
                false: REC_OFF
            }
        }
    ]);

    async function onStop(blobUrl) {
        try {
            const formData = await getAudioFormData(blobUrl)
            const response = await axios.post('http://localhost:5000/receive_command', formData)
            const { object, action } = response.data

            handleSuccess(action, object);
        } catch {
            toast.error("Erro ao processar o comando. Tente novamente")
        }
    }

    async function getAudioFormData(blobUrl) {
        const audioBlob = await (await fetch(blobUrl)).blob()
        const audio = new File([audioBlob], 'audio.wav', { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('audio', audio);

        return formData;
    }


    function handleSuccess(action, object) {
        toast.success(`Comando processado com sucesso. Atuando sobre: ${object}`);

        const actionStatus = ['ligar', 'abrir', 'iniciar'].includes(action);
        const newObjects = objects.map(item => {
            return {
                ...item,
                status: item.name === object ? actionStatus : item.status
            }
        })

        setObjects(newObjects)
    }


    return (
        <>
            <main>
                <div className="buttons">
                    <button onClick={startRecording} disabled={status === 'recording'}>Iniciar Gravação</button>
                    <button onClick={stopRecording} disabled={status !== 'recording'}>Interromper Gravação</button>
                </div>
                <div className="images">
                    {objects.map((object, index) => (
                        <img key={index} src={object.img[`${object.status}`]}/>
                    ))}
                </div>
                <ToastContainer/>
            </main>
        </>
    )
}

export default App
