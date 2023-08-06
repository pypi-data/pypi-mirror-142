from cloudmesh.catalog.convert import Convert
from cloudmesh.catalog.manager import ServiceManager
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.shell.command import map_parameters


class CatalogCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_catalog(self, args, arguments):
        """
        ::

          Usage:
                catalog info
                catalog start [--docker] [--name=NAME]
                catalog stop [--docker] [--name=NAME] [--pid=PID]
                catalog status [--docker] [--name=NAME]
                catalog list
                catalog default [--name=NAME]
                catalog init  DIR [--name=NAME] [--port=PORT] [--docker]
                catalog query QUERY [--name=NAME]
                catalog table --attributes=ATTRIBUTES [--name=NAME]
                catalog print [--format=FORMAT] [--name=NAME]
                catalog copy [--docker] [--name=NAME] [--source=URL]
                catalog federate [--docker] [--name=NAME] [--source=URL]
                catalog load [--docker] [--name=NAME] [--source=URL]
                catalog export bibtex [--source=SOURCE] [--destination=DESTINATION]
                catalog export md [--source=SOURCE] [--destination=DESTINATION]
                catalog export hugo [--source=SOURCE] [--destination=DESTINATION]
                catalog export --template=TEMPLATE [--source=SOURCE] [--destination=DESTINATION]
                catalog check [--source=SOURCE]

          This command manages the catalog service.

          Arguments:
              DIR   the directory path containing the entries

          Options:
              --docker     docker
              --name=NAME  the name of the entry
              --port=PORT  the port

          Description:

            catalog list
              lists all available catalog services. There could be multiple
              catalog services

            catalog default [--name=NAME]
              sets the default catalog server to the given name.
              The names of all services is stored in a yaml file at
              ~/.cloudmesh/catalog.services.yaml

              > cloudmesh:
              >  catalog:
              >    - name: my-service-a
              >      mode: native
              >      port: 10000
              >    - name: my-service-a
              >      mode: docker
              >      port: 10001

            catalog init  DIR [--name=NAME] [--port=PORT] [--docker]
                This command initializes a given catalog service, while using the
                directory DIR as a content dir for the entries.
                The dir can have multiple subdirectories for better organization.
                Each subdirectory name is automatically a "tag" in the entry.
                Note that it will be added to any tag that is in the entry. If
                the tag is already in the entry it will be ignored.

                The name is the name of the catalog to identify it in case
                multiple catalogs exist

                The port is the port number. The number is identified from the catalog list and is the next
                available port if it is not already used. If no prior catalog service with a port exists
                the port 40000 will be used

                If the docker flag is specified the catalog will not be started natively, but in a
                docker container. uid and gid will be automatically forwarded to the container, so data changes are
                conducted with the host user.

                If the image does not exist, a docker container will be started. The Dockerfile is located in the code
                base and dynamically retrieved from the pip installed package in
                cloudmesh/catalog/Dockerfile

            catalog query QUERY [--name=NAME]
              issues a query to the given catalog services. If the name is omitted the default service is used
              The query is formulated using https://jmespath.org/tutorial.html

            catalog print [--format=FORMAT] [--name=NAME]
                prints all entries of the given catalogs. With attributes you can select a number of attributes.
                If the attributes ae nested a . notation can be used
                The format is by default table, but can also set to json, yaml, csv

            catalog start [--docker] [--name=NAME]
                This command starts the services. If docker is used the service is started
                as container. The name specifies the service so multiple services can be started
                If the name is omitted the default container is used. If only one service is specified
                this is the default

            catalog stop [--docker] [--name=NAME]
                This command stops the services. If docker is used the service is stopped
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog status [--docker] [--name=NAME]
                This command gets that status of the services. If docker is used the service is stopped
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog copy [--docker] [--name=NAME] [--source=URL]
                This command copies the contents from all catalogs specified by the
                source urls. Please note that the URLs are of teh form host:port
                However it can also load data from a file or directory when specified as
                file://path. Relative path can be specified as file::../data

            catalog federate [--docker] [--name=NAME] [--source=URL]
                This command federates the contents from all catalogs specified by the
                source urls. Please note that the URLs are of teh form host:port.
                When the federation service is queried, parallel queries will be issued to
                all sources and the query result will be reduced to a single result.
                when the cache option is specified the result will be cached and the next
                time the query is asked it will use also the cached result. A time to live
                is specified to asure the cached result will be deleted after the ttl is expired.

            catalog load [--docker] [--name=NAME] [--source=URL]
                In contrast to the copy command, the LOAD command reads the data from
                directories or files and not from URLs
                However, copy can also do file://path

            catalog export bibtex [--source=SOURCE] [--destination=DESTINATION]
                Exports the information from the catalog as a single bibtex file
                If a name is specified only the named entries are exported.
                The format of the entries will be

                > @misc{id,
                >   author={the author field of the entry},
                >   title={the title of the entry},
                >   abstract={the description of the entry},
                >   url={the url of the entry},
                >   howpublished={Wb Page},
                >   month={the month of the date the entry was created},
                >   year={the year of the date when the entry was created}
                > }

            catalog export md [--source=SOURCE] [--destination=DESTINATION]
                Exports the information from the catalog as a directory tree
                equivalent to the original.
                If a name is specified only the named entries are exported.
                The format of the entries will be

                > # {title}
                >
                > {author}
                >
                > ## Description
                >
                > {description}
                >
                > and so on

            catalog export hugo [--source=SOURCE] [--destination=DESTINATION]

                Format of the entry

                > ---
                > title: "Running GPU Batch jobs on Rivanna"
                > linkTitle: "GPU@Rivanna"
                > author: {author of the technology}
                > date: 2017-01-05
                > weight: 4
                > description: >
                >   Short Description of the entry
                > ---
                >
                > {{% pageinfo %}}
                > Short description from the entry
                > {{% /pageinfo %}}
                > ## Description
                >
                > {description}
                >
                > and so on

            catalog export --template=TEMPLATE [--source=SOURCE] [--destination=DESTINATION]

                formats the source file(s) based on the template that is provided.
                The template is a file that uses curly brakets for replacement of
                the attribute names, If a name is not in the source an error will
                be produced.

            catalog check [--source=SOURCE]
                does some elementary checking an all files in the directory tree
                starting with SOURCE
        """
        map_parameters(arguments,
                       "directory",
                       "attributes",
                       "docker",
                       "name",
                       "pid",
                       "source",
                       "destination")
        # format can not be mapped into a dict as reserved word use
        # arguments["--format"] instead


        if arguments["list"]:
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.init:
            # requires the catalog server and the location of a named
            # catalog in ~/.cloudmesh/catalog/{name}
            # so if we find one we could create some default and use that catalog
            # as default and if no name is specified we use that
            # this is to be implemented in the init function
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.query:
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.table:
            # attributes = split(arguments.attributes,",")
            # print(attributes)
            # TODO Catalog not imported
            # catalog = Catalog()
            # print(Printer.write(catalog.data,header=attributes))
            raise NotImplementedError

        elif arguments["--format"]:
            kind = arguments["--format"]
            # TODO not implemented
            print(kind)
            raise NotImplementedError

        elif arguments.start:
            service = ServiceManager()
            service.start()

        elif arguments.stop:

            service = ServiceManager()
            if arguments.pid:
                service.stop(pid=int(arguments.pid))
            else:
                service.stop()

        elif arguments.status:
            service = ServiceManager()
            print(service.status())

        elif arguments.info:
            service = ServiceManager()
            print(service.info())

        elif arguments.bibtex and arguments.export:

            #  catalog export bibtex [--source=SOURCE] [--destination=DESTINATION]

            VERBOSE(arguments)

            if arguments.desitination is not None:
                print("Destination not yet implemented")
                return ""
            else:
                source = arguments.source
                convert = Convert()
                convert.bibtex(sources=source)

        elif arguments.hugo:

            source = arguments.source
            convert = Convert()
            convert.hugo_markdown(sources=source)

        elif arguments.md:

            source = arguments.source
            convert = Convert()
            convert.markdown(sources=source)

        elif arguments.template:

            template = arguments.template
            source = arguments.source
            convert = Convert()
            convert.template(sources=source, template=template)

        elif arguments.check:
            convert = Convert()
            convert.yaml_check(source=arguments.source)

        return ""
