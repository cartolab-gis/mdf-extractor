# MDF Extractor

The MDF Extractor takes any valid MDF file or MDF and LDF file and outputs a series of csv files based on the non-system tables in the schema.

## Sponsored by:

<a href="https://regrid.com/"><img src="./public/regrid_RT_green.svg" width="400" alt="Regrid Logo"></a>

## Requirements

This utility requires docker and docker-compose.

## Usage

### <span style="color:red">**_WARNING_**: </span>The MDF files and resulting CSVs can be many gigabytes in size. Ensure you have proper space on your system.

Extract your _.mdf and _.ldf (if available) to the ./MDF directory.

Once the file has been extracted to the MDF directory, from the root directory where docker-compose.yaml is located, run:

```bash
# you may need to run with sudo priveleges
docker-compose up

```

After the database has been created and attached the utility will start to output csv files in the CSV folder. Once complete, in the terminal you will see:

```bash
All scripts have been executed. Waiting for MS SQL(1) to terminate.

```

While the container is still running, you can connect to the database using SSMS with the user `sa` and password `LocalPassword123!`.

<span style="color:red">**_WARNING_**: </span> Do not use this database for anything other than checking and exploring the data.

And you can close the utility with Ctrl-C. Finally,

```bash
# you may need to run with sudo priveleges
docker-compose down
```

## Output

The utility will spit out csv files into the CSV directory.

## Clean Up

When done using the utility, it is suggested to delete all files in the MDF directory so that there is no confusion on future runs. The _.mdf and _.ldf files are linked after running, so be sure to clear both.
