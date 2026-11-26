Every backup copy will be locked against change or deletion until its retention expires, even by a fully privileged account. StorageGRID's S3 Object Lock and immutable Blob storage hold each one in compliance mode. Copies leave the data center on two paths, to the alternate site and to US Gov Arizona, so no single site or region holds them all.

A spill caught in a locked copy cannot be edited out. It is sanitized instead by destroying that backup set's key, which leaves the copy unreadable.
