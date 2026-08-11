--- 
--- ## Query name:
--- GeneProduct-IDs.sql
--- 
--- ## Query creation date:
--- 2021-06-04
--- 
--- ## Data Version:
--- RegulonDB v10.8	 ECOCYC: v24.0
--- 
--- ## Description:
--- Information about Gene-Product external databases Identifiers
--- 
--- 
--- ## Author:
--- Hely Salgado
--- 
--- ## Requested by:
--- Claire
--- 
--- ## Query Details
--- 
--- GENE : table with the genes from Ecocyc and RegulonDB
--- GENE_PRODUCT_LINK : Link between gene and product
--- PRODUCT : Product table
--- OBJECT_SYNONYM: gene and product synonyms
--- object_external_db_link: IDs in other external databases related to the gene or product
--- external_db : info about of the external databases like the name
--- 
SELECT distinct g.gene_id,
        g.gene_name,
        g.gene_posleft,
        g.gene_posright,
        g.gene_strand,
        NVL((                 -- extrayendo los sinonimos del gene ordenados por nombre
        SELECT LISTAGG(object_synonym_name, ',') WITHIN GROUP (ORDER BY object_synonym_name)
        FROM(
            SELECT object_synonym_name
            FROM  OBJECT_SYNONYM O
            WHERE  o.object_id = g.gene_id
        )),' ') AS GENE_SYNONYMS,
        (                     -- identificadores de otras bases de datos para el gene
        SELECT LISTAGG(e.external_db_name || ':' || oe.ext_reference_id || ', ') WITHIN GROUP (ORDER BY oe.ext_reference_id)
        FROM   object_external_db_link oe,
               external_db e
        WHERE  oe.external_db_id = e.external_db_id and
               oe.object_id = g.gene_id
        ) as identifiers_gene,
        p.product_id,
        p.product_name,
        NVL(( 
        SELECT LISTAGG(object_synonym_name, ',') WITHIN GROUP (ORDER BY object_synonym_name)
        FROM (
          SELECT object_synonym_name
          FROM  OBJECT_SYNONYM O
          WHERE  o.object_id = p.product_id
        )),' ') AS PRODUCT_SYNONYMS,
        (                 -- identificadores de otras bases de datos para el producto
        SELECT LISTAGG(e.external_db_name || ':' || oe.ext_reference_id || ', ') WITHIN GROUP (ORDER BY oe.ext_reference_id)
        FROM   object_external_db_link oe,
               external_db e
        WHERE  oe.external_db_id = e.external_db_id and
               oe.object_id = p.product_id
        ) as identifiers_product
FROM    gene g,
        gene_product_link gpl,
        product p
WHERE  g.gene_id = gpl.gene_id AND
       gpl.product_id = p.product_id
ORDER BY g.gene_posleft

