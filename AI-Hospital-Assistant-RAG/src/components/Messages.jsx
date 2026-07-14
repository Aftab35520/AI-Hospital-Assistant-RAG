import React from "react";
import ReactMarkdown from "react-markdown";

export default function Messages({ msg, role }) {
  const isUser = role === "user";

  return (
    <div className={`flex w-full mb-4 ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`
          max-w-[75%]
          px-5
          py-4
          rounded-2xl
          shadow-md
          break-words
          ${
            isUser
              ? "bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-br-md"
              : "bg-white border border-gray-200 text-gray-800 rounded-bl-md"
          }
        `}
      >
        {!isUser && (
          <div className="flex items-center gap-3 mb-3 pb-2 border-b border-gray-200">
            <div className="h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
              AI
            </div>

            <div>
              <h2 className="font-semibold text-gray-900 leading-none">
                Hospital AI Assistant
              </h2>
              <p className="text-xs text-gray-500 mt-1">
                Sunrise Multispeciality Hospital
              </p>
            </div>
          </div>
        )}

        <div className="text-[15px] leading-6">
          <ReactMarkdown
            components={{
              h1: ({ children }) => (
                <h1 className="text-2xl font-bold mb-2">{children}</h1>
              ),

              h2: ({ children }) => (
                <h2 className="text-xl font-semibold mt-3 mb-1">
                  {children}
                </h2>
              ),

              h3: ({ children }) => (
                <h3 className="text-lg font-semibold mt-2 mb-1">
                  {children}
                </h3>
              ),

              p: ({ children }) => (
                <p className="mb-1 leading-6">{children}</p>
              ),

              ul: ({ children }) => (
                <ul className="list-disc pl-5 my-1">
                  {children}
                </ul>
              ),

              ol: ({ children }) => (
                <ol className="list-decimal pl-5 my-1">
                  {children}
                </ol>
              ),

              li: ({ children }) => (
                <li className="mb-0.5 leading-6">{children}</li>
              ),

              strong: ({ children }) => (
                <strong
                  className={`font-semibold ${
                    isUser ? "text-white" : "text-blue-600"
                  }`}
                >
                  {children}
                </strong>
              ),

              code: ({ children }) => (
                <code
                  className={`px-1 py-0.5 rounded text-sm ${
                    isUser
                      ? "bg-blue-700 text-white"
                      : "bg-gray-100 text-red-600"
                  }`}
                >
                  {children}
                </code>
              ),
            }}
          >
            {msg}
          </ReactMarkdown>
        </div>
      </div>
    </div>
  );
}