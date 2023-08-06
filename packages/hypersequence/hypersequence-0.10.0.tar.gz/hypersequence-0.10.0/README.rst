HyperSequence is a data format and library for super-fast training of large machine learning datasets. HyperSequence aims to be much faster than conventional data pipelining solutions, especially with larger records.

Features:

* Simple API to write datasets
* Supports multiple inputs and outputs per training record
* Functions for rebatching, randomization and splitting
* tensorflow.keras integration

Links:

* Documentation: https://hypersequence.readthedocs.io
* Gitlab page: https://gitlab.com/vvanbeveren/hypersequence

Usage
-----

Building a dataset
``````````````````

To write create a ``HyperSequenceWriter`` and call ``.append(inputs=..., outputs=...)`` for every row you wish to add to the dataset.

.. code-block:: python

    import hypersequence as hs
    import numpy as np

    test_file = "/data/myset.hsq"
    batch_size = 16
    no_of_recs = 10000

    with hs.HyperSequenceWriter(test_file, batch_size) as hsw:
        for i in range(no_of_recs):
            inp = np.random.random((10, 10))
            out = np.random.random((2, 10, 2))
            hsw.append(inputs=inp, outputs=out)


Note that ``HyperSequenceWriter`` has a native batch-size granularity. It will be optimized for this batch-size. Though it is possible to deviate from this batch-size, this comes at a (often small) performance penalty. Moreover, batch-sizes are constrained to either a divider or multiple of the native batch-size.

Training the dataset using tensorflow.keras
```````````````````````````````````````````

Training with HyperSequence is also straight-forward. Create a ``HyperSequenceFile`` and use ``KerasSequence`` wrapper class to feed it to the Fit function.

.. code-block:: python

    import hypersequence as hs
    import numpy as np
    import tensorflow.keras as tfk

    test_file = "/data/myset.hsq"

    with hs.HyperSequenceFile(test_file) as hsq:
        (inp_dtype,), (out_dtype,) = hsq.dtypes()

        model = tfk.models.Sequential(
            [
                tfk.layers.InputLayer(input_shape=inp_dtype.shape),
                tfk.layers.Flatten(),
                tfk.layers.Dense(np.prod(out_dtype.shape), activation='relu'),
                tfk.layers.Reshape(out_dtype.shape)
            ]
        )
        model.compile(optimizer='adam', loss='mean_squared_error')

        model.fit(
            hsq.as_keras(shuffle_on_epoch=True),
            epochs=16
        )


Note the ``shuffle_on_epoch`` can be used to randomize the order of the dataset before each epoch.

Multi-Input/Multi-Output
````````````````````````
HyperSequence supports multi-input/output for more complex training datasets.

.. code-block:: python

    import hypersequence as hs
    import numpy as np

    test_file = "/data/myset.hsq"
    batch_size = 16
    no_of_recs = 10000

    with hs.HyperSequenceWriter(test_file, batch_size) as hsw:
        for i in range(no_of_recs):
            inp1 = np.random.random((10, 10))
            inp2 = np.random.random(100)
            inp3 = np.random.random((3, 3, 3))
            out1 = np.random.random((2, 10, 2))
            out2 = np.random.random((100))
            hsw.append(inputs=(inp1, inp2, inp3), outputs=(out1, out2))

Splitting the dataset into training and validation
``````````````````````````````````````````````````

Using ``HyperSequence.split()`` you can split the dataset into multiple sub-sets.

Here is the same example as above, but with splitting.

.. code-block:: python

    import hypersequence as hs
    import numpy as np
    import tensorflow.keras as tfk

    test_file = "/data/myset.hsq"

    with hs.HyperSequenceFile(test_file) as hsq:
        train, validation = hsq.split(0.8)

        (inp_dtype,), (out_dtype,) = hsq.dtypes()

        model = tfk.models.Sequential(
            [
                tfk.layers.InputLayer(input_shape=inp_dtype.shape),
                tfk.layers.Flatten(),
                tfk.layers.Dense(np.prod(out_dtype.shape), activation='relu'),
                tfk.layers.Reshape(out_dtype.shape)
            ]
        )
        model.compile(optimizer='adam', loss='mean_squared_error')

        model.fit(
            train.as_keras(shuffle_on_epoch=True),
            epochs=16,
            validation_data=validation.as_keras()
        )

Changing the batch-size
```````````````````````

.. code-block:: python

    import hypersequence as hs
    import tensorflow.keras as tfk

    test_file = "/data/myset.hsq"

    with hs.HyperSequenceFile(test_file) as hsq:
        # Rebatch from 16 records to 64 records.
        hsq64 = hsq.rebatch(64)
        # Split for training and validation
        train, validation = hsq64.split(0.8)

        # create model as before....
        model = ...

        # Train!
        model.fit(
            train.as_keras(shuffle_on_epoch=True),
            epochs=16,
            validation_data=validation.as_keras()
        )


HyperSequenceFile creation options
----------------------------------

use_mmap
````````
A ``HyperSequenceFile`` by default uses mmap to map the file to memory, for speed and efficiency. However, this has a few draw-backs, first the data from the produced arrays can not be used when the HyperSequence is closed. Second, it may use up a lot of OS resources, or behave different depending on the backing filesystem. For this reason there you can disable the mmap operation using ``use_mmap=False`` as an argument to the ``HyperSequenceFile`` constructor. If there are strange problems, try to disable this first. In multi-threading context, disabling mmap may require ``thread_safe=True``.

copy_buffer
```````````
A second option is ``copy_buffer``, This option copies the buffer from mmap into memory. This allows the usage of the buffer outside of the contxt manager. Set ``copy_buffer=True`` to use the returned arrays from outside of the context manager. ``copy_buffer`` is only useful when mmap is enabled. *May* resolve some concurrency issues, while still being faster compared to disabling mmap.

thread_safe
```````````
By default, HyperSequenceFile does not enforce thread-safety, though when using mmap this may be done by the OS. However, when using multi-threading and/or multi-gpu training it may be needed.



