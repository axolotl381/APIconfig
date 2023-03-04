import multiprocessing
import os

bind="127.0.0.1:28168"

worker_class = "uvicorn.workers.UvicornWorker"
workers = 4
