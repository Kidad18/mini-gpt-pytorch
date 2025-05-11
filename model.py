import { useState } from 'react';
import { Code, PlayCircle, Brain, Settings, BookOpen, Cpu } from 'lucide-react';

export default function MiniGPTPreview() {
  const [activeTab, setActiveTab] = useState('overview');
  
  return (
    <div className="flex flex-col h-full w-full bg-gray-50 rounded-lg shadow-lg overflow-hidden">
      {/* Header */}
      <div className="bg-indigo-600 text-white p-4">
        <h1 className="text-2xl font-bold flex items-center">
          <Brain className="mr-2" /> Mini GPT Implementation
        </h1>
        <p className="text-indigo-100 mt-1">A lightweight transformer-based text generation model</p>
      </div>
      
      {/* Navigation Tabs */}
      <div className="flex bg-indigo-800 text-white">
        <button 
          className={`p-3 px-4 flex items-center ${activeTab === 'overview' ? 'bg-indigo-700 border-b-2 border-white' : 'hover:bg-indigo-700'}`}
          onClick={() => setActiveTab('overview')}>
          <BookOpen size={18} className="mr-2" /> Overview
        </button>
        <button 
          className={`p-3 px-4 flex items-center ${activeTab === 'architecture' ? 'bg-indigo-700 border-b-2 border-white' : 'hover:bg-indigo-700'}`}
          onClick={() => setActiveTab('architecture')}>
          <Cpu size={18} className="mr-2" /> Architecture
        </button>
        <button 
          className={`p-3 px-4 flex items-center ${activeTab === 'config' ? 'bg-indigo-700 border-b-2 border-white' : 'hover:bg-indigo-700'}`}
          onClick={() => setActiveTab('config')}>
          <Settings size={18} className="mr-2" /> Configuration
        </button>
        <button 
          className={`p-3 px-4 flex items-center ${activeTab === 'demo' ? 'bg-indigo-700 border-b-2 border-white' : 'hover:bg-indigo-700'}`}
          onClick={() => setActiveTab('demo')}>
          <PlayCircle size={18} className="mr-2" /> Demo
        </button>
      </div>
      
      {/* Content Area */}
      <div className="flex-1 p-5 overflow-auto">
        {activeTab === 'overview' && (
          <div>
            <h2 className="text-xl font-bold mb-3">Mini GPT Implementation</h2>
            <p className="mb-4">
              This code implements a small-scale GPT (Generative Pre-trained Transformer) model from scratch using PyTorch.
              It features the core components of modern language models while remaining compact and educational.
            </p>
            
            <div className="bg-white p-4 rounded-lg shadow-sm mb-4">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Key Features</h3>
              <ul className="list-disc pl-5 space-y-1">
                <li>Complete transformer architecture</li>
                <li>Self-attention mechanism with multiple heads</li>
                <li>Auto-regressive text generation</li>
                <li>Configurable architecture parameters</li>
                <li>Simple training pipeline</li>
              </ul>
            </div>
            
            <div className="bg-white p-4 rounded-lg shadow-sm">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Use Cases</h3>
              <ul className="list-disc pl-5 space-y-1">
                <li>Educational tool for understanding transformers</li>
                <li>Starting point for custom language model implementations</li>
                <li>Playground for experimenting with attention mechanisms</li>
                <li>Basis for text generation projects</li>
              </ul>
            </div>
          </div>
        )}
        
        {activeTab === 'architecture' && (
          <div>
            <h2 className="text-xl font-bold mb-3">Model Architecture</h2>
            
            <div className="bg-white p-4 rounded-lg shadow-sm mb-4">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Components</h3>
              
              <div className="mb-3">
                <h4 className="font-bold text-indigo-500">Self-Attention Head</h4>
                <p className="text-gray-700">Implements the key-query-value attention mechanism that allows the model to focus on relevant parts of the input.</p>
              </div>
              
              <div className="mb-3">
                <h4 className="font-bold text-indigo-500">Multi-Head Attention</h4>
                <p className="text-gray-700">Combines multiple attention heads to capture different aspects of relationships between tokens.</p>
              </div>
              
              <div className="mb-3">
                <h4 className="font-bold text-indigo-500">Feed-Forward Network</h4>
                <p className="text-gray-700">Two-layer neural network applied to each position independently.</p>
              </div>
              
              <div className="mb-3">
                <h4 className="font-bold text-indigo-500">Transformer Block</h4>
                <p className="text-gray-700">Combines attention and feed-forward networks with residual connections and layer normalization.</p>
              </div>
              
              <div>
                <h4 className="font-bold text-indigo-500">MiniGPT</h4>
                <p className="text-gray-700">The complete model with token embeddings, positional embeddings, and the output projection layer.</p>
              </div>
            </div>
            
            <div className="bg-gray-100 p-4 rounded-lg flex justify-center">
              <div className="bg-white p-4 rounded shadow-sm max-w-md">
                <div className="text-center text-sm text-gray-500 mb-2">Architecture Diagram</div>
                <div className="border p-3 rounded">
                  <div className="bg-blue-100 p-2 rounded text-center mb-2">Input Embeddings + Positional Encoding</div>
                  <div className="bg-indigo-100 p-2 rounded text-center mb-2">Transformer Block × {2}</div>
                  <div className="bg-purple-100 p-2 rounded text-center mb-2">Layer Norm</div>
                  <div className="bg-pink-100 p-2 rounded text-center">Linear Head → Softmax</div>
                </div>
              </div>
            </div>
          </div>
        )}
        
        {activeTab === 'config' && (
          <div>
            <h2 className="text-xl font-bold mb-3">Configuration</h2>
            
            <div className="bg-white p-4 rounded-lg shadow-sm mb-4">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Hyperparameters</h3>
              
              <div className="grid grid-cols-2 gap-3">
                <div className="border rounded p-3">
                  <div className="font-bold text-indigo-500">block_size</div>
                  <div className="text-2xl">8</div>
                  <div className="text-sm text-gray-500">Context window length</div>
                </div>
                
                <div className="border rounded p-3">
                  <div className="font-bold text-indigo-500">batch_size</div>
                  <div className="text-2xl">4</div>
                  <div className="text-sm text-gray-500">Training batch size</div>
                </div>
                
                <div className="border rounded p-3">
                  <div className="font-bold text-indigo-500">n_embd</div>
                  <div className="text-2xl">32</div>
                  <div className="text-sm text-gray-500">Embedding dimension</div>
                </div>
                
                <div className="border rounded p-3">
                  <div className="font-bold text-indigo-500">n_heads</div>
                  <div className="text-2xl">4</div>
                  <div className="text-sm text-gray-500">Number of attention heads</div>
                </div>
                
                <div className="border rounded p-3">
                  <div className="font-bold text-indigo-500">n_layers</div>
                  <div className="text-2xl">2</div>
                  <div className="text-sm text-gray-500">Number of transformer blocks</div>
                </div>
                
                <div className="border rounded p-3">
                  <div className="font-bold text-indigo-500">learning_rate</div>
                  <div className="text-2xl">1e-3</div>
                  <div className="text-sm text-gray-500">AdamW optimizer</div>
                </div>
              </div>
            </div>
            
            <div className="bg-white p-4 rounded-lg shadow-sm">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Dataset</h3>
              <div className="p-3 bg-gray-100 rounded font-mono text-sm">
                text = "hello world"
              </div>
              <p className="mt-2 text-gray-700">
                A minimal dataset used for demonstration purposes. The model learns patterns from this short text.
              </p>
            </div>
          </div>
        )}
        
        {activeTab === 'demo' && (
          <div>
            <h2 className="text-xl font-bold mb-3">Model Demo</h2>
            
            <div className="bg-white p-4 rounded-lg shadow-sm mb-4">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Training Progress</h3>
              
              <div className="space-y-2">
                <div className="flex items-center">
                  <div className="w-24">Step 0:</div>
                  <div className="flex-1 bg-gray-200 rounded-full h-4">
                    <div className="bg-red-500 h-4 rounded-full" style={{width: '100%'}}></div>
                  </div>
                  <div className="ml-2">Loss: 2.0418</div>
                </div>
                
                <div className="flex items-center">
                  <div className="w-24">Step 100:</div>
                  <div className="flex-1 bg-gray-200 rounded-full h-4">
                    <div className="bg-yellow-500 h-4 rounded-full" style={{width: '25%'}}></div>
                  </div>
                  <div className="ml-2">Loss: 0.0555</div>
                </div>
                
                <div className="flex items-center">
                  <div className="w-24">Step 200:</div>
                  <div className="flex-1 bg-gray-200 rounded-full h-4">
                    <div className="bg-green-400 h-4 rounded-full" style={{width: '10%'}}></div>
                  </div>
                  <div className="ml-2">Loss: 0.0188</div>
                </div>
                
                <div className="flex items-center">
                  <div className="w-24">Step 300:</div>
                  <div className="flex-1 bg-gray-200 rounded-full h-4">
                    <div className="bg-green-500 h-4 rounded-full" style={{width: '5%'}}></div>
                  </div>
                  <div className="ml-2">Loss: 0.0094</div>
                </div>
                
                <div className="flex items-center">
                  <div className="w-24">Step 400:</div>
                  <div className="flex-1 bg-gray-200 rounded-full h-4">
                    <div className="bg-green-600 h-4 rounded-full" style={{width: '3%'}}></div>
                  </div>
                  <div className="ml-2">Loss: 0.0066</div>
                </div>
              </div>
            </div>

            <div className="bg-white p-4 rounded-lg shadow-sm">
              <h3 className="font-bold text-lg mb-2 text-indigo-600">Text Generation</h3>
              
              <div className="p-4 bg-black text-green-400 font-mono rounded">
                <div>$ python model.py</div>
                <div className="text-gray-400"># Training output...</div>
                <div>Step 0, Loss: 2.0418</div>
                <div>Step 100, Loss: 0.0555</div>
                <div>Step 200, Loss: 0.0188</div>
                <div>Step 300, Loss: 0.0094</div>
                <div>Step 400, Loss: 0.0066</div>
                <div className="mt-2">Generated Text: hello world hello world</div>
                <div className="animate-pulse">_</div>
              </div>
              
              <p className="mt-3 text-gray-700">
                The model has learned to generate text in the style of its training data. Since it was trained on "hello world", 
                it repeats this pattern with some variations.
              </p>
            </div>
          </div>
        )}
      </div>
      
      {/* Footer */}
      <div className="bg-gray-100 p-3 border-t flex justify-between items-center">
        <div className="flex items-center text-gray-600">
          <Code size={16} className="mr-1" />
          <span className="text-sm">PyTorch Implementation</span>
        </div>
        <div className="text-xs text-gray-500">
          A Mini GPT Transformer Model
        </div>
      </div>
    </div>
  );
}
