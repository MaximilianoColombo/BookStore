import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
//import reactJsx from 'vite-react-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
